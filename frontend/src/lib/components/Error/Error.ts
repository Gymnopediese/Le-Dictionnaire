import { writable } from "svelte/store";

export const errorStore = writable<string | null>(null);

let timeout: any;

export function ERROR(message: string, duration = 5000) {
	clearTimeout(timeout);
	errorStore.set(message);

	timeout = setTimeout(() => {
		errorStore.set(null);
	}, duration);
}