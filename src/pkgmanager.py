"""

class PackageManagerAPI:
    def __init__(self):
        self.package_manager = self.detect_package_manager()

    def detect_package_manager(self):
        package_managers = {
            "apt": "/usr/bin/apt-get",
            "dnf": "/usr/bin/dnf",
            "yum": "/usr/bin/yum",
            "pacman": "/usr/bin/pacman",
            "zypper": "/usr/bin/zypper",
            "apk": "/sbin/apk"
        }

        for manager, path in package_managers.items():
            if os.path.exists(path):
                return manager
        return None

    def install_package(self, package_name):
        if self.package_manager == "apt":
            # Implement apt package installation
            pass
        elif self.package_manager == "dnf":
            # Implement dnf package installation
            pass
        elif self.package_manager == "yum":
            # Implement yum package installation
            pass
        elif self.package_manager == "pacman":
            # Implement pacman package installation
            pass
        elif self.package_manager == "zypper":
            # Implement zypper package installation
            pass
        elif self.package_manager == "apk":
            # Implement apk package installation
            pass
        else:
            print("Unsupported package manager.")

    # Similarly, you can define functions for other package manager operations like remove, update, etc.

# Example usage
package_manager_api = PackageManagerAPI()
package_manager_api.install_package("example-package")

I have to do this....
"""


import apt_pkg
import dnf
import os

def __install_package_apt(package_name):
    cache = apt_pkg.Cache()
    if cache.get_pkg(package_name) is None:
        print(f"Package \'{package_name}\'wasn't found. ")
        return
    
    pkg = cache[package_name]
    if pkg.current_state != apt_pkg.CURSTATE_NOT_INSTALLED:
        print(f"Package {package_name} is already installed.")
        return
    
    apt_pkg.init_system()
    cache.update()
    cache.open()
    
    try:
        pkg.mark_install()
        cache.commit()
        print(f"Package {package_name} installed with success.")
    except SystemError as e:
        print(f"Error to install package {package_name}: {e}")

def __install_package_dnf(package_name):
    base = dnf.Base()
    base.fill_sack()
    try:
        base.install(package_name)
        base.resolve()
        base.do_transaction()
        print(f"The package {package_name} was installed successfully!")
    except dnf.exceptions.Error as e:
        print(f"Error to install package {package_name}: {e}")

def __removePackage_dnf(package_name):
    try:
        base = dnf.Base()
        base.read_all_repos()
        base.remove(package_name)
        base.resolve()
        base.download_packages(base.transaction.install_set)
        base.do_transaction()

    except dnf.exceptions.Error as e:
        print("An error occurred when finalizing the transaction.", e)

    finally:
        if base:
            base.close()

def __removePackage_apt(package_name):
    try:
        apt_pkg.init()
        cache = apt_pkg.Cache()
        if cache[package_name].is_installed:
            cache[package_name].mark_delete()
            cache.commit()
            print(f'The package "{package_name}" was removed successfully.')
        else:
            print(f'The package "{package_name}" is not installed.')
    except Exception as e:
        print("An error occurred while removing the package", e)
    finally:
        apt_pkg.cleanup()

def __detect_package_manager():
    try:
        package_managers = {
            "apt": "/usr/bin/apt-get",
            "dnf": "/usr/bin/dnf",
            "yum": "/usr/bin/yum",
            "pacman": "/usr/bin/pacman",
            "zypper": "/usr/bin/zypper",
            "apk": "/sbin/apk"
        }

        for manager, path in package_managers.items():
            if os.path.exists(path):
                return manager

    except Exception as e:
        print("An error occurred during package manager detection:", e)

    return None



