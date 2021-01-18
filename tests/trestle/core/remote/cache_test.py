# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Testing for cache functionality."""

import pathlib
import pytest
import random
import string
from urllib import parse
from unittest.mock import patch

import trestle.core.err as err
from trestle.core import generators
from trestle.core.err import TrestleError
from trestle.core.remote import cache
from trestle.oscal.catalog import Catalog


def test_fetcher_base():
    """Test whether fetcher can get an object from the cache."""
    pass


def test_github_fetcher():
    """Test the github fetcher."""
    pass


def test_local_fetcher(tmp_trestle_dir):
    """Test the local fetcher."""
    rand_str = ''.join(random.choice(string.ascii_letters) for x in range(16))
    catalog_file = pathlib.Path(tmp_trestle_dir / f'{rand_str}.json').__str__()
    catalog_data = generators.generate_sample_model(Catalog)
    catalog_data.oscal_write(pathlib.Path(catalog_file))
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), catalog_file, False, False)
    fetcher._refresh = True
    rc = fetcher._update_cache()
    assert fetcher._inst_cache_path.exists()


def test_sftp_get_fails(tmp_trestle_dir):
    """Test sftp fetcher failing sftp client get."""
    uri = 'sftp://some.host//path/to/test.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), uri, False, False)
    fetcher._refresh = True
    fetcher._cache_only = False
    with patch('asyncssh.SFTPClient.get') as sftp_get_mock:
        sftp_get_mock.side_effect = Exception
        with pytest.raises(TrestleError):
            fetcher._update_cache()


def test_sftp_run_client_fails(tmp_trestle_dir):
    """Test sftp fetcher failing sftp run_client method and asyncssh start connection calls."""
    uri = 'sftp://some.host//path/to/test.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), uri, False, False)
    fetcher._refresh = True
    fetcher._cache_only = False
    with patch('trestle.core.remote.cache.SFTPFetcher._run_client') as run_client_mock:
        run_client_mock.side_effect = Exception
        with pytest.raises(Exception):
            fetcher._update_cache()
    with patch('asyncssh.connect') as asyncssh_connect_mock:
        asyncssh_connect_mock.side_effect = Exception
        with pytest.raises(Exception):
            fetcher._update_cache()
    with patch('asyncssh.SSHClientConnection.start_sftp_client') as start_sftp_client_mock:
        start_sftp_client_mock.side_effect = Exception
        with pytest.raises(Exception):
            fetcher._update_cache()


def test_sftp_fetcher(tmp_trestle_dir):
    """Test sftp fetcher with mocked success."""
    uri = 'sftp://some.host//path/to/test.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), uri, False, False)
    fetcher._refresh = True
    fetcher._cache_only = False
    with patch('asyncssh.SFTPClient.get') as sftp_get_mock:
        sftp_get_mock.return_value = None
        try:
            fetcher._update_cache()
        except Exception:
            AssertionError()
        else:
            assert True


def test_sftp_fetcher_cache_only(tmp_trestle_dir):
    """Test sftp fetcher with cache only set true."""
    uri = 'sftp://some.host//path/to/test.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), uri, False, False)
    fetcher._refresh = True
    fetcher._cache_only = True
    with patch('asyncssh.SFTPClient.get') as sftp_get_mock:
        sftp_get_mock.return_value = None
        try:
            fetcher._update_cache()
        except Exception:
            AssertionError()
        else:
            assert True


def test_fetcher_bad_uri(tmp_trestle_dir):
    """Test fetcher factory with bad URI."""
    for uri in [
            '',
            'https://',
            'https:///blah.com',
            'sftp://',
            '..',
            'sftp://blah.com',
            'sftp:///path/to/file.json',
            'sftp://user:pass@hostname.com\\path\\to\\file.json',
            'sftp://:pass@hostname.com/path/to/file.json'
    ]:
        with pytest.raises(TrestleError):
            fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), uri, False, False)


def test_fetcher_factory(tmp_trestle_dir: pathlib.Path) -> None:
    """Test that the fetcher factory correctly resolves functionality."""
    local_uri_1 = 'file:///home/user/oscal_file.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), local_uri_1, False, False)
    assert type(fetcher) == cache.LocalFetcher

    local_uri_2 = '/home/user/oscal_file.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), local_uri_2, False, False)
    assert type(fetcher) == cache.LocalFetcher

    local_uri_3 = '../../file.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), local_uri_3, False, False)
    assert type(fetcher) == cache.LocalFetcher

    sftp_uri = 'sftp://user@hostname:/path/to/file.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), sftp_uri, False, False)
    assert type(fetcher) == cache.SFTPFetcher

    sftp_uri_2 = 'sftp://user@hostname:2000/path/to/file.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), sftp_uri_2, False, False)
    assert type(fetcher) == cache.SFTPFetcher

    https_uri = 'https://host.com/path/to/json.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), https_uri, False, False)
    assert type(fetcher) == cache.HTTPSFetcher

    https_basic_auth = 'https://user:pass@host.com/path/to/json.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), https_basic_auth, False, False)
    assert type(fetcher) == cache.HTTPSFetcher

    github_url_1 = 'https://github.com/some/url.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), github_url_1, False, False)
    assert type(fetcher) == cache.GithubFetcher

    github_url_2 = 'https://user:auth@github.com/some/url.json'
    fetcher = cache.FetcherFactory.get_fetcher(pathlib.Path(tmp_trestle_dir), github_url_2, False, False)
    assert type(fetcher) == cache.GithubFetcher
