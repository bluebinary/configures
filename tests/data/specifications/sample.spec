# This file lists the library's required environment variables, and optionally may
# include a regular expression along with each required variable, that the configured
# variable value must match in order for library initialisation to succeed. If a
# required variable is missing or has an unexpected value an exception will be raised.
# Optional environment variables may also be included for the purpose of validating
# their values against the provided regular expression. Optional variables are denoted
# with a special "?" prefix on their environment variable names.

# Application Time Zone
TZ=([A-Za-z\_]+\/[A-Za-z\_])[America/Los_Angeles]
