def spreadsheet_safe(value):
    """Keep untrusted text from being interpreted as a spreadsheet formula."""
    if not isinstance(value, str):
        return value
    if value.startswith(("\t", "\r", "\n")) or value.lstrip(" \t\r\n").startswith(("=", "+", "-", "@")):
        return "'" + value
    return value
