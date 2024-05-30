import dagger
from dagger import dag, function

@function
async def nuclei_scan(targets: str, templates: str, output: str) -> str:
    """
    Scan the specified targets using nuclei templates and save the results to the specified output file.

    Args:
        targets (str): A string containing the targets to scan.
        templates (str): A string containing the nuclei templates to use.
        output (str): The file path to save the scan results.

    Returns:
        str: A message indicating the completion of the scan process.
    """
    return await (
        dag.container()
        .from_("projectdiscovery/nuclei")
        .with_mounted_file("/targets.txt", targets)
        .with_mounted_file("/templates", templates)
        .with_workdir("/")
        .with_exec(["nuclei", "-l", "/targets.txt", "-t", "/templates", "-o", output])
        .stdout()
    )
