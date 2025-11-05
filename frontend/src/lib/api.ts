import { goto } from "$app/navigation";
import { cookies, remove_cookie,  } from "./cookies";

function preprotection()
{
    if (!cookies.token)
    {
        goto("/")
        return false
    }
    return true;
}

export async function ping()
{
    return await get("/ping");
}

function protection(result: Response) {

    if (result.status == 401)
    {
        remove_cookie("token")
        goto("/")
        throw new Error("Unauthorized")
    }
    if (result.status >= 400)
    {
        throw new Error("Error: " + result.status + " " + result.statusText)
    }
    return result.json();

}

export async function get(route: string)
{

    if (!preprotection()) return
    var result = await fetch("/api" + route, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + cookies.token,
        },
    })
    return protection(result);
}

export async function put(route: string, body: any)
{
    if (!preprotection()) return
    var result = await fetch("/api" + route, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + cookies.token,
        },
        body: JSON.stringify(body)
    })
    return protection(result);
}

export async function post(route: string, body: any)
{
    if (!preprotection()) return
    var result = await fetch("/api" + route, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': "Bearer " + cookies.token,
        },
        body: JSON.stringify(body)
    })
    return protection(result);
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
    return protection(result);
}