import { get, put } from "./api"
import { get_writable, user } from "./global";


var dictionnaire : any = {

}

export async function get_dictionnaire(id: number) : Promise<any>
{
    if (dictionnaire[id] != undefined)
        return dictionnaire[id]
    dictionnaire[id] = await get("/dictionnaires/" + id);
    dictionnaire[id].termes = await get("/dictionnaires/" + id + "/termes?sort_by=ctime");
    return dictionnaire[id];
}

var dictionnaires : any = {

}

export async function get_dictionnaires(user_id="", args = "") : Promise<any>
{
    var key = user_id +args
    if (key == "")
        key = "feed";
    if (dictionnaires[key] != undefined)
        return dictionnaires[key]
    if (user_id == "me")
    {
        dictionnaires[key] = await get(`/me/dictionnaires?${args}`);
        user.update((v)=> {v.dictionnaires = dictionnaires[key]; return v;})
    }
    if (key == "feed")
    {
        dictionnaires[key] = await get(`/dictionnaires/?${args}`);
    } 
    return dictionnaires[key];
}

var user_: any = {}

export async function get_user(id)
{
    if (id == "me" || id == get_writable(user).id)
        return get_writable(user)
    if (user_[id] != undefined)
        return user_[id];
    user_[id] = await get(`/users/${id}`)
    console.log(user_[id])
    return user_[id]
}

var users: any = {}

export async function get_users(user_id="", args = "")
{
    var key = user_id + args
    if (users[key] != undefined)
        return users[key];
    
    if (user_id == "me" || user_id == get_writable(user).id)
    {
        users[key] = await get(`/me/users?${args}`)
        return users[key]
    }
    users[user_id] = await get(`/users?${user_id}`)
    return users[key]
}



export async function follow_dictionnaire(dictionnaire, user_id="me") {
    await put(`/dictionnaires/${dictionnaire.id}/ownerships/${user_id}`, {"rights": "read"})
}
export async function unfollow_dictionnaire(dictionnaire, user_id="me") {
    await put(`/dictionnaires/${dictionnaire.id}/ownerships/${user_id}`, {"rights": "read"})
}

export async function unwrite_dictionnaire(dictionnaire, user_id="me") {
    await put(`/dictionnaires/${dictionnaire.id}/ownerships/${user_id}`, {"rights": "read"})
}


export async function follow_user(id) {
    await put(`/users/${id}/relationship`, {"type": "follow"})
}

export async function unfollow_user(id) {
    await put(`/users/${id}/relationship`, {"type": "unfollow"})
}

export async function unblock_user(id) {
    await put(`/users/${id}/relationship`, {"type": "unblock"})
}
