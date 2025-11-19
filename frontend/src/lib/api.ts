import { goto } from "$app/navigation";
import { cookies, remove_cookie,  } from "./cookies";

export async function ping()
{
    return await get("/ping");
}

function preprotection()
{
    if (!cookies.token)
    {
        goto("/login")
        return false
    }
    return true;
}

async function protection(result: Response, token_needed: boolean = true) {

    if (result.status == 401 && token_needed)
    {
        remove_cookie("token")
        goto("/")
        throw new Error("Unauthorized")
    }
    if (result.status >= 400)
    {
        throw await result.json();
    }
    return await result.json();

}

export async function get(route: string, token_needed: boolean = true)
{

    if (!preprotection() && token_needed) return
    //"https://api.dictionnaire.kofl.ch" 
    var result = await fetch("https://api.dictionnaire.kofl.ch" + route, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + cookies.token,
        },
    })
    return await protection(result, token_needed);
}

export async function put(route: string, body: any, token_needed: boolean = true)
{
    if (!preprotection() && token_needed) return
    var result = await fetch("/api" + route, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + cookies.token,
        },
        body: JSON.stringify(body)
    })
    return await protection(result, token_needed);
}

export async function post(route: string, body: any, token_needed: boolean = false)
{
    if (!preprotection() && token_needed) return
    var result = await fetch("/api" + route, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + cookies.token,
        },
        body: JSON.stringify(body)
    })
    return await protection(result, token_needed);
}

export async function del(route: string)
{
    if (!preprotection()) return
    var result = await fetch("/api" + route, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + cookies.token,
        },
    })
    return await protection(result);
}