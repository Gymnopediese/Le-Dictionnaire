import { genres } from "./enums";



export function get_radio_button_checked(buttons)
{
    for (let button of buttons)
    {
        if (button.checked)
        {
            return button.value;
        }
    }
}
