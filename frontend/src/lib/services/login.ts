import { goto } from "$app/navigation";
import { get, post } from "./api";
import { remove_cookie, set_cookie } from "$lib/services/cookies";
import { user } from "./global";

export async function signin(username: String, password: String)
{
    var token = await post("/auth/signin", {username, password}, false);
    set_cookie("token", token.token);
    user.set(await get("/me/"))
    goto("/")
    return token;
}

export async  function signup(username: String, password: String, repeat: String)
{
    if (password != repeat)
        throw ("Error: password does not match");
    var token = await post("/auth/signup", {username, password}, false);
    set_cookie("token", token.token);
    user.set(await get("/me/"))
    goto("/")
    return token;
}

export async  function signout()
{
    remove_cookie("token")
    location.href = "/"
}