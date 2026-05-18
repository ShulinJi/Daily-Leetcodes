deps = {
    "engine_v3": ["network_v2", "infotainment_v2"],
    "network_v2": ["infotainment_v1"]
}

current = {
    "engine": "v1",
    "network": "v1",
    "infotainment": "v1"
}

desired = {
    "engine": "v3"
}

print(resolve_updates(deps, current, desired))




# O(V + E) time, O(V) space where V is the number of packages and E is the number of dependencies
def parse_package(package):
    parts = package.split("_")
    name = parts[0]
    version = parts[1]
    return name, version


def resolve_updates(deps, current, desired):
    result = current.copy()

    def dfs(package):
        name, version = parse_package(package)

        # already installed
        if result.get(name) == version:
            return

        # install dependencies first
        if package in deps:
            for dep in deps[package]:
                dfs(dep)

        # then install this package
        result[name] = version

    for name in desired:
        version = desired[name]
        package = name + "_" + version
        dfs(package)

    return result