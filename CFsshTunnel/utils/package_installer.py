from logging import raiseExceptions
from operator import ifloordiv
from struct import pack
import apt
import sys
import subprocess


def apt_package_installer(package_name: str):
    """
    Checks for package and installs if needed
    Parameters
        package_name(str): name of the package to be installed
    """
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    print("Checking for " + package_name)
    pkg = cache[package_name]

    if pkg.is_installed:
        print("{pkg_name} already installed".format(pkg_name=package_name))
    else:
        print(
            "Installing {pkg_name} through apt-get".format(pkg_name=package_name))
        pkg.mark_install()
        try:
            cache.commit()
        except Exception as arg:
            print >> sys.stderr, "{pkg_name} installation failed [{err}]".format(
                pkg_name=package_name, err=str(arg))


def deb_package_installer(package_name: str, package_url: str):
    """
    Downloads and installs .deb pack from specified url
    """
    cache = apt.Cache()
    package_installed = False
    if package_name in cache:
        package_installed = cache[package_name].is_installed
        
    if package_installed:
                print("{pkg_name} already installed".format(pkg_name=package_name))
    else:
        print("Installing {pkg_name}".format(pkg_name=package_name))
        url_split = package_url.split('/')
        deb_name = url_split[-1]
        try:
            subprocess.call(["wget", package_url])
            subprocess.call(["sudo", "dpkg", "-i", deb_name])
            subprocess.call(["sudo", "rm", "-f", deb_name])
        except:
            raise RuntimeError("Failed to install package {pkg_name}".format(pkg_name=package_name))