"""
This file was auto-generated by an ObjectFactory of aTLAS
"""


NAME = 'Basic Topic Scenario'


AGENTS = ['A', 'B', 'C', 'D']


OBSERVATIONS = [{'authors': ['A'],
                 'before': [],
                 'details': {'content_trust.topics': ['Web Engineering'],
                             'uri': 'http://example.com/Redecentralization_of_the_Web'},
                 'message': 'Redecentralization of the Web',
                 'observation_id': 1,
                 'receiver': 'B',
                 'sender': 'A'},
                {'authors': ['A'],
                 'before': [1],
                 'details': {'content_trust.topics': ['Web Engineering'],
                             'uri': 'http://example.com/Web_of_Things'},
                 'message': 'Web of Things',
                 'observation_id': 2,
                 'receiver': 'B',
                 'sender': 'A'},
                {'authors': ['A'],
                 'before': [2],
                 'details': {'content_trust.topics': ['Web Engineering'],
                             'uri': 'http://example.com/Web_Assembly'},
                 'message': 'Web Assembly',
                 'observation_id': 3,
                 'receiver': 'B',
                 'sender': 'A'},
                {'authors': ['C'],
                 'before': [3],
                 'details': {'content_trust.topics': ['Web Engineering'],
                             'uri': 'http://example.com/Semantic_Web_and_Linked_Open_Data'},
                 'message': 'Semantic Web and Linked Open Data',
                 'observation_id': 4,
                 'receiver': 'B',
                 'sender': 'C'},
                {'authors': ['C'],
                 'before': [4],
                 'details': {'content_trust.topics': ['Web Engineering'],
                             'uri': 'http://example.com/Redecentralization_of_the_Web'},
                 'message': 'Redecentralization of the Web',
                 'observation_id': 5,
                 'receiver': 'B',
                 'sender': 'C'},
                {'authors': ['C'],
                 'before': [5],
                 'details': {'content_trust.topics': ['Web Engineering'],
                             'uri': 'http://example.com/Web-based_learning'},
                 'message': 'Web-based learning',
                 'observation_id': 6,
                 'receiver': 'B',
                 'sender': 'C'}]


HISTORY = {'A': [['B', 'http://example.com/Web_Assembly', 1.0],
                 ['C', 'http://example.com/Web_of_Things', 1.0],
                 ['D', 'http://example.com/Semantic_Web_and_Linked_Open_Data', 1.0]],
           'B': [['A', 'http://example.com/Redecentralization_of_the_Web', 0.0],
                 ['C', 'http://example.com/Web_of_Things', 0.0],
                 ['D', 'http://example.com/Web_Assembly', 1.0]],
           'C': [['A', 'http://example.com/Redecentralization_of_the_Web', 1.0],
                 ['B', 'http://example.com/Redecentralization_of_the_Web', 1.0],
                 ['D', 'http://example.com/Web-based_learning', 1.0]],
           'D': [['A', 'http://example.com/Web_of_Things', 1.0],
                 ['B', 'http://example.com/Web_Assembly', 1.0],
                 ['C', 'http://example.com/Semantic_Web_and_Linked_Open_Data', 1.0]]}


SCALES_PER_AGENT = {'A': {'cooperation': 0.5,
                          'default': 0.0,
                          'forgivability': -0.5,
                          'maximum': 1.0,
                          'minimum': -1.0,
                          'name': 'Trust Scale by Marsh and Briggs (2009)',
                          'package': 'marsh_briggs_scale'},
                    'B': {'cooperation': 0.5,
                          'default': 0.0,
                          'forgivability': -0.5,
                          'maximum': 1.0,
                          'minimum': -1.0,
                          'name': 'Trust Scale by Marsh and Briggs (2009)',
                          'package': 'marsh_briggs_scale'},
                    'C': {'cooperation': 0.5,
                          'default': 0.0,
                          'forgivability': -0.5,
                          'maximum': 1.0,
                          'minimum': -1.0,
                          'name': 'Trust Scale by Marsh and Briggs (2009)',
                          'package': 'marsh_briggs_scale'},
                    'D': {'cooperation': 0.5,
                          'default': 0.0,
                          'forgivability': -0.5,
                          'maximum': 1.0,
                          'minimum': -1.0,
                          'name': 'Trust Scale by Marsh and Briggs (2009)',
                          'package': 'marsh_briggs_scale'}}


METRICS_PER_AGENT = {'A': {'__final__': {'name': 'weighted_average', 'weights': {}},
                           'content_trust.authority': ['C'],
                           'content_trust.direct_experience': {},
                           'content_trust.popularity': {},
                           'content_trust.recommendation': {},
                           'content_trust.topic': {'B': {'Web Engineering': 1.0},
                                                   'C': {'Web Engineering': 1.0},
                                                   'D': {'Web Engineering': 1.0}}},
                     'B': {'__final__': {'name': 'weighted_average', 'weights': {}},
                           'content_trust.authority': ['C'],
                           'content_trust.direct_experience': {},
                           'content_trust.popularity': {},
                           'content_trust.recommendation': {},
                           'content_trust.topic': {'A': {'Web Engineering': 0.5},
                                                   'C': {'Web Engineering': 0.5},
                                                   'D': {'Web Engineering': 1.0}}},
                     'C': {'__final__': {'name': 'weighted_average', 'weights': {}},
                           'content_trust.authority': [],
                           'content_trust.direct_experience': {},
                           'content_trust.popularity': {},
                           'content_trust.recommendation': {},
                           'content_trust.topic': {'A': {'Web Engineering': 1.0},
                                                   'B': {'Web Engineering': 1.0},
                                                   'D': {'Web Engineering': 1.0}}},
                     'D': {'__final__': {'name': 'weighted_average', 'weights': {}},
                           'content_trust.authority': ['C'],
                           'content_trust.direct_experience': {},
                           'content_trust.popularity': {},
                           'content_trust.recommendation': {},
                           'content_trust.topic': {'A': {'Web Engineering': 1.0},
                                                   'B': {'Web Engineering': 1.0},
                                                   'C': {'Web Engineering': 1.0}}}}


DESCRIPTION = 'This is a basic scenario with four agents, one authority and a topic metric.'
