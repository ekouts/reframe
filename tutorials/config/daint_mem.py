# Copyright 2016-2024 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# and other ReFrame Project Developers. See the top-level LICENSE file for
# details.
#
# SPDX-License-Identifier: BSD-3-Clause


site_configuration = {
    'systems': [
        {
            'name': 'daint',
            'descr': 'Piz Daint Supercomputer',
            'hostnames': ['daint'],
            'modules_system': 'tmod32',
            'partitions': [
                {
                    'name': 'login',
                    'descr': 'Login nodes',
                    'scheduler': 'local',
                    'launcher': 'local',
                    'environs': ['builtin', 'gnu', 'intel', 'nvidia', 'cray']
                },
                # rfmdocstart: memory
                {
                    'name': 'gpu',
                    'descr': 'Hybrid nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-C gpu', '-A csstaff'],
                    'environs': ['gnu', 'intel', 'nvidia', 'cray'],
                    'max_jobs': 100,
                    'resources': [
                        {
                            'name': 'memory',
                            'options': ['--mem={size}']
                        }
                    ]
                },
                # rfmdocend: memory
                {
                    'name': 'mc',
                    'descr': 'Multicore nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['-C mc', '-A csstaff'],
                    'environs': ['gnu', 'intel', 'nvidia', 'cray'],
                    'max_jobs': 100
                }
            ]
        }
    ]
}
