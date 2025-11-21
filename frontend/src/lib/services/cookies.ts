
export var cookies = {}
var loaded = false
export function load_cookies()
{
    if (loaded)
        return loaded
    loaded = true
    var _cookies = document.cookie.split("; ")
    if (document.cookie == "")
        return;
    for (let cookie of _cookies)
    {
        let cookie_split = cookie.split("=")
        cookies[cookie_split[0]] = cookie_split[1]
    }
    return false
}

// export function save_cookies()
// {
//     for (const [key, value] of Object.entries(cookies))
//     {
//         document.cookie = key + "=" + value + "; path=/; "
//         //TODO: "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
//     }
// }

export function remove_cookie(key)
{
    delete cookies[key];
    document.cookie = key + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

export function set_cookie(key: String, val: String)
{
    cookies[key] = val;
    document.cookie = key + "=" + val + "; path=/;";
}