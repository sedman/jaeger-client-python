# Copyright (c) 2016 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, unicode_literals, print_function

from . import __version__

import six

# Max number of bits to use when generating random ID
MAX_ID_BITS = 64

# How often remotely controller sampler polls for sampling strategy
DEFAULT_SAMPLING_INTERVAL = 60

# How often remote reporter does a preemptive flush of its buffers
DEFAULT_FLUSH_INTERVAL = 1

# Name of the HTTP header used to encode trace ID
TRACE_ID_HEADER = 'uber-trace-id' if six.PY3 else b'uber-trace-id'

# Prefix for HTTP headers used to record baggage items
BAGGAGE_HEADER_PREFIX = 'uberctx-' if six.PY3 else b'uberctx-'

# The name of HTTP header or a TextMap carrier key which, if found in the
# carrier, forces the trace to be sampled as "debug" trace. The value of the
# header is recorded as the tag on the # root span, so that the trace can
# be found in the UI using this value as a correlation ID.
DEBUG_ID_HEADER_KEY = 'jaeger-debug-id'

JAEGER_CLIENT_VERSION = 'Python-%s' % __version__

# Tracer-scoped tag that tells the version of Jaeger client library
JAEGER_VERSION_TAG_KEY = 'jaeger.version'

# Tracer-scoped tag that contains the hostname
JAEGER_HOSTNAME_TAG_KEY = 'jaeger.hostname'

# the type of sampler that always makes the same decision.
SAMPLER_TYPE_CONST = 'const'

# the type of sampler that polls Jaeger agent for sampling strategy.
SAMPLER_TYPE_REMOTE = 'remote'

# the type of sampler that samples traces with a certain fixed probability.
SAMPLER_TYPE_PROBABILISTIC = 'probabilistic'

# the type of sampler that samples only up to a fixed number
# of traces per second.
# noinspection SpellCheckingInspection
SAMPLER_TYPE_RATE_LIMITING = 'ratelimiting'

# the type of sampler that samples only up to a fixed number
# of traces per second.
# noinspection SpellCheckingInspection
SAMPLER_TYPE_LOWER_BOUND = 'lowerbound'
