"""Constants used by Python Arlo."""

# API Endpoints
API_URL = "https://my.arlo.com"

DEVICE_SUPPORT_ENDPOINT = API_URL + "/hmsweb/devicesupport/v2"
SUBSCRIBE_ENDPOINT = API_URL + "/hmsweb/client/subscribe"
UNSUBSCRIBE_ENDPOINT = API_URL + "/hmsweb/client/unsubscribe"
BILLING_ENDPOINT = API_URL + "/hmsweb/users/serviceLevel/v2"
DEVICES_ENDPOINT = API_URL + "/hmsweb/users/devices"
FRIENDS_ENDPOINT = API_URL + "/hmsweb/users/friends"
LIBRARY_ENDPOINT = API_URL + "/hmsweb/users/library"
LOGIN_ENDPOINT = "https://ocapi-app.arlo.com/api/auth"
LOGOUT_ENDPOINT = API_URL + "/hmsweb/logout"
NOTIFY_ENDPOINT = API_URL + "/hmsweb/users/devices/notify/{0}"
PROFILE_ENDPOINT = API_URL + "/hmsweb/users/profile"
RESET_ENDPOINT = LIBRARY_ENDPOINT + "/reset"
RESET_CAM_ENDPOINT = RESET_ENDPOINT + "/?uniqueId={0}"
STREAM_ENDPOINT = API_URL + "/hmsweb/users/devices/startStream"
SNAPSHOTS_ENDPOINT = API_URL + "/hmsweb/users/devices/fullFrameSnapshot"

# number of days to preload video
PRELOAD_DAYS = 30

# modes not returned with the Arlo API's available modes
FIXED_MODES = {
    'schedule': 'true'
}

# define resources
RESOURCES = {
    'base_station': 'base_station',
    'modes': 'modes',
    'schedule': 'schedule',
    'rules': 'rules',
    'cameras': 'cameras',
}

# define body used when executing an action
ACTION_BODY = {
    'action': None,
    'from': None,
    'properties': None,
    'publishResponse': None,
    'resource': None,
    'to': None
}

# define body used for live_streaming
STREAMING_BODY = {
    'action': 'set',
    'from': None,
    'properties': {'activityState': 'startPositionStream'},
    'publishResponse': 'true',
    'resource': None,
    'to': None,
    'transId': "",
}


# define body used for live_streaming
SNAPSHOTS_BODY = {
    'action': 'set',
    'from': None,
    'properties': {'activityState': 'fullFrameSnapshot'},
    'publishResponse': 'true',
    'resource': None,
    'to': None,
    'transId': ""
}

# vim:sw=4:ts=4:et:
