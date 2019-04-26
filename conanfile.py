import os
import json
from conans import ConanFile, CMake


def get_version():
    project_settings = os.path.join(os.path.dirname(__file__), "ProjectSettings.json")
    with open(project_settings) as json_file:  
        data = json.load(json_file)
    version = '{}.{}.{}'.format(data['version_major'], data['version_minor'], data['version_subminor'])
    return version


class MyLibrary(ConanFile):
    name = "lightfoot-iprc"
    version = get_version()

    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "build_tests": [True, False]}
    default_options = {"shared": False,
                       "build_tests": False}
    generators = "cmake_find_package"

    scm = {"type": "git",
           "url": "https://github.com/jgsogo/issue-4795.git",  # I need this because I have my remote with git@github.com:jgsogo/issue-4795.git
           "revision": "auto"}

    exports = "ProjectSettings.json"  # This file has to be exported (it is needed by the recipe)

    def requirements(self):
        self.requires("zlib/1.2.8@conan/stable")

    def sources(self):
        # Nothing to do here, your sources will be cloned using the `scm` data
        pass

    def imports(self):
        # If you are not going to repackage this files, or you don't need it in
        #   your local folder during build, do not import from your dependencies.
        pass

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTS"] = self.options.build_tests
        cmake.configure(source_folder="src")
        cmake.build()
    