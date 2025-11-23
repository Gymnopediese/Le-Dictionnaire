import { get } from "./api"


var dictionnaire : any = {

}

export async function get_dictionnaire(id: number) : Promise<any>
{
    if (dictionnaire[id] != undefined)
        return dictionnaire[id]
    dictionnaire[id] = await get("/dictionnaires/" + id);
    return dictionnaire[id];
}