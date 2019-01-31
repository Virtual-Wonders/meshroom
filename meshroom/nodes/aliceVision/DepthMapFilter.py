__version__ = "2.0"

from meshroom.core import desc


class DepthMapFilter(desc.CommandLineNode):
    commandLine = 'aliceVision_depthMapFiltering {allParams}'
    gpu = desc.Level.NORMAL
    size = desc.DynamicNodeSize('input')
    parallelization = desc.Parallelization(blockSize=10)
    commandLineRange = '--rangeStart {rangeStart} --rangeSize {rangeBlockSize}'

    inputs = [
        desc.File(
            name='input',
            label='Input',
            description='SfMData file.',
            value='',
            uid=[0],
        ),    
        desc.File(
            name="depthMapsFolder",
            label="Depth Maps Folder",
            description="Input depth maps folder",
            value="",
            uid=[0],
        ),
        desc.FloatParam(
            name='minViewAngle',
            label='Min View Angle',
            description='Minimum angle between two views.',
            value=2.0,
            range=(0.0, 10.0, 0.1),
            uid=[0],
            advanced=True,
        ),
        desc.FloatParam(
            name='maxViewAngle',
            label='Max View Angle',
            description='Maximum angle between two views.',
            value=70.0,
            range=(10.0, 120.0, 1),
            uid=[0],
            advanced=True,
        ),
        desc.IntParam(
            name="nNearestCams",
            label="Number of Nearest Cameras",
            description="Number of nearest cameras used for filtering.",
            value=10,
            range=(0, 20, 1),
            uid=[0],
            advanced=True,
        ),
        desc.IntParam(
            name="minNumOfConsistentCams",
            label="Min Consistent Cameras",
            description="Min Number of Consistent Cameras",
            value=3,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.IntParam(
            name="minNumOfConsistentCamsWithLowSimilarity",
            label="Min Consistent Cameras Bad Similarity",
            description="Min Number of Consistent Cameras for pixels with weak similarity value",
            value=4,
            range=(0, 10, 1),
            uid=[0],
        ),
        desc.IntParam(
            name="pixSizeBall",
            label="Filtering Size in Pixels",
            description="Filtering size in pixels",
            value=0,
            range=(0, 10, 1),
            uid=[0],
            advanced=True,
        ),
        desc.IntParam(
            name="pixSizeBallWithLowSimilarity",
            label="Filtering Size in Pixels Bad Similarity",
            description="Filtering size in pixels",
            value=0,
            range=(0, 10, 1),
            uid=[0],
            advanced=True,
        ),
        desc.BoolParam(
            name='computeNormalMaps',
            label='Compute Normal Maps',
            description='Compute normal maps per depth map.',
            value=False,
            uid=[],
            advanced=True,
        ),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='''verbosity level (fatal, error, warning, info, debug, trace).''',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output',
            description='Output folder for generated depth maps.',
            value=desc.Node.internalFolder,
            uid=[],
        ),
    ]
