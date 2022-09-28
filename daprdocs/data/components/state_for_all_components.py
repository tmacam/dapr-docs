from dataclasses import dataclass
import pathlib
import yaml
from operator import itemgetter

YAML_SUFFIX_LENGTH = len('.yaml')

@dataclass
class Component:
    building_block: str
    provider: str
    component: str
    state: str
    version: str
    since: str



def main():
    all_components: list[Component] = []
    cur_dir = pathlib.Path('.')
    all_building_blocks_dirs = [x for x in cur_dir.iterdir() if x.is_dir()]
    for building_block_dir in  all_building_blocks_dirs:
        building_block_name = building_block_dir.name
        for provider_path in [x for x in building_block_dir.glob('*.yaml')]:
            provider_name = provider_path.parts[-1][0:-YAML_SUFFIX_LENGTH]
            with provider_path.open() as fh:
                provider_info = yaml.safe_load(fh)
                for implementation in provider_info:
                    i = Component(
                        building_block=building_block_name,
                        provider=provider_name,
                        component=implementation['component'],
                        state=implementation['state'],
                        version=implementation['version'],
                        since=(implementation.get('since') or '?'),
                    )
                    #print(i)
                    all_components.append(i)

    #print(all_components)
    print("\t".join(['building_block', 'provider', 'component', 'state', 'version']))
    for c in all_components:
        print("\t".join([c.building_block, c.provider, c.component, c.state, c.version]))


if __name__ == '__main__':
    main()