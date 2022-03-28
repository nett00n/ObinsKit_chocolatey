from bs4 import BeautifulSoup
from jinja2 import Template
import hashlib
import os
import re
import requests


def main():
    global github_prefix
    github_prefix = "https://github.com/"
    github_user = "obinskit"
    github_repo = "obinskit"

    html_data = get_data_from_url("https://www.hexcore.xyz/obinskit")
    latest_version = get_latest_version_from_html(html_data)
    win32_url = get_download_url_from_html("ia32.exe", html_data, latest_version)
    win32_hashsum = get_sha256_from_url(win32_url)
    win64_url = get_download_url_from_html("x64.exe", html_data, latest_version)
    win64_hashsum = get_sha256_from_url(win64_url)
    render_choco_files(latest_version, win64_url, win32_url, win64_hashsum, win32_hashsum)

def get_sha256_from_url(url):
    r = requests.get(url)
    with open('tmp_file', 'wb') as f:
        f.write(r.content)
    with open('tmp_file',"rb") as f:
        bytes = f.read()
        readable_hash = hashlib.sha256(bytes).hexdigest();
    if os.path.exists('tmp_file'):
        os.remove('tmp_file')
    return(readable_hash)

def render_choco_files(latest_version, win64_url, win32_url, win64_hashsum, win32_hashsum):
    nuspec_xml = define_nuspec_template()
    nuspec_xml_text = nuspec_xml.render(latest_version = latest_version)
    # print(nuspec_xml_text)
    file = open('obinskit.nuspec', 'w')
    file.write(nuspec_xml_text)
    file.close()
    chocolateyinstall_ps1 = define_chocolateinstall_template()
    chocolateyinstall_ps1_text = chocolateyinstall_ps1.render(win32_url = win32_url, win32_hashsum = win32_hashsum, win64_url = win64_url, win64_hashsum = win64_hashsum)
    file = open('tools/chocolateyinstall.ps1', 'w')
    file.write(chocolateyinstall_ps1_text)
    file.close()
    # print(chocolateyinstall_ps1_text)

def define_nuspec_template():
    with open("templates/nuspec.j2") as f:
        template_text = f.read()

    jinja_template = Template(template_text)
    return(jinja_template)

def define_chocolateinstall_template():
    with open("templates/chocolateyinstall.ps1.j2") as f:
        template_text = f.read()
    jinja_template = Template(template_text)
    return(jinja_template)

def get_data_from_url(RemoteURL):
    data = requests.get(RemoteURL)
    RemoteData = re.sub(r"><", ">\n<", data.text)
    return(RemoteData)


def get_download_url_from_html(keyphrase, html_data, version):
    url = ""
    soup = BeautifulSoup(html_data, 'lxml')
    urls = soup.find_all('a', class_='mx-5 text-primary')
    for url in urls:
        url = str(url)
        if keyphrase not in url:
            continue
        url = url.split('"')
        url = url[3]
        print(url)
        return(url)

def get_latest_version_from_html(html_data):
    version = ''
    soup = BeautifulSoup(html_data, 'lxml')
    urls = soup.find_all('a', class_='mx-5 text-primary')
    version = str(urls[1])
    version = version.split('"')
    version = version[3]
    version = version.split("_")
    version = version[1]
    return(version)


if __name__ == "__main__":
    main()