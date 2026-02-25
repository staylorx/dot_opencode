#!/usr/bin/env python3
"""
Initialize a new Melos workspace with clean architecture structure.
"""

import os
import shutil
import yaml


def init_workspace():

    # TODO: Update pubspec.yaml now
    #
    # # Create melos.yaml
    # melos_config = {
    #     "name": "my_project",
    #     "packages": ["packages/*"],
    #     "command": {"bootstrap": {"dependencies": ["flutterfire"]}},
    # }
    # with open("melos.yaml", "w") as f:
    #     yaml.dump(melos_config, f)

    # Create packages directory structure
    os.makedirs("packages/core/lib/src", exist_ok=True)
    os.makedirs("packages/domain_entities/lib/src", exist_ok=True)
    os.makedirs("packages/domain_contracts/lib/src", exist_ok=True)
    os.makedirs("packages/domain_usecases/lib/src", exist_ok=True)
    os.makedirs("packages/datasource_sembast/lib/src", exist_ok=True)
    os.makedirs("packages/presentation/lib/src", exist_ok=True)

    print("Melos workspace initialized with clean architecture structure.")


if __name__ == "__main__":
    init_workspace()
