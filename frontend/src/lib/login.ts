import { goto } from "$app/navigation";
import { post } from "./api";
import { set_cookie } from "./cookies";

export async function signin(username: String, password: String)
{
    var token = await post("/auth/signin", {username, password}, false);
    console.log("token", token)
    set_cookie("token", token.token);
    goto("/menu")
    return token;
}

export async  function signup(username: String, password: String, repeat: String)
{
    if (password != repeat)
        throw ("Error: password does not match");
    var token = await post("/auth/signup", {username, password}, false);
    console.log(token)
    set_cookie("token", token.token);
    goto("/menu")
    return token;
}