import requests

# Returns list with first item being app status (CATEGORIES_SUPPORT) and others being notes about compatibility
def get_deck_game_status(app_id: int):
    CATEGORIES_SUPPORT = {1: "Unsupported", 2: "Playable", 3: "Verified"}
    CATEGORIES_COMMENTS = {1: "Note", 2: "Fail", 3: "Info", 4: "Checkmark"}

    request = requests.get(
        f"https://store.steampowered.com/saleaction/ajaxgetdeckappcompatibilityreport?nAppID={app_id}")

    json = request.json()
    app_id
    category_raw = json['results']['resolved_category']
    category = CATEGORIES_SUPPORT[category_raw]
    comments = [category]
    for i in json['results']['resolved_items']:
        comments.append(
            (CATEGORIES_COMMENTS[i['display_type']], i['loc_token'][30:]))
    return comments


# Returns app name by id or None if none such id exists
def get_app_id(name: str):
    request = requests.get(
        f"https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    a = request.json()['applist']['apps']
    name_lower = name.lower()
    for i in a:
        if i['name'].lower() == name_lower:
            return i['appid']
    return None
