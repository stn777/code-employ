import { camelCase, transform, snakeCase } from "lodash";

export async function getApi<T>(url: string, param: any): Promise<T> {
  const response = await fetch(`${url}/${param}`).catch(error => {
    throw new Error(error);
  });
  return handleResponse<T>(response);
}

export async function postApi<T>(url: string, body: any): Promise<T> {
  const response = await fetch(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(camelCaseToSnakeCase(body))
  }).catch(error => {
    throw new Error(error);
  });
  return handleResponse<T>(response);
}

export async function putApi<T>(url: string, body: any): Promise<T> {
  const response = await fetch(url, {
    method: "PUT",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(camelCaseToSnakeCase(body))
  }).catch(error => {
    throw new Error(error);
  });
  return handleResponse<T>(response);
}

export async function deleteApi<T>(url: string, param: any): Promise<T> {
  const response = await fetch(`${url}/${param}`, {
    method: "DELETE"
  }).catch(error => {
    throw new Error(error);
  });
  return handleResponse<T>(response);
}

function handleResponse<T>(response: Response) {
  if (!response.ok) throw new Error(response.statusText);
  return response.json().then(json => {
    return snakeCaseToCamelCase(json) as T;
  });
}

//TODO: add a proper parser in the backend to allow the frontend to be used with any backend
const snakeCaseToCamelCase = (json: any): Object =>
  transform(json, (result: any, value: any, key: string) => {
    result[camelCase(key)] =
      value instanceof Object ? snakeCaseToCamelCase(value) : value;
  });

const camelCaseToSnakeCase = (json: Object): Object =>
  transform(json, (result: any, value: any, key: string) => {
    result[snakeCase(key)] =
      value instanceof Object ? camelCaseToSnakeCase(value) : value;
  });
