export async function get<T>(url: string, params: any): Promise<T> {
  const response = await fetch(url).catch(error => {
    throw new Error(error);
  });
  return handleResponse<T>(response);
}

export async function post<T>(url: string, body: any): Promise<T> {
  const response = await fetch(url, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body)
  }).catch(error => {
    throw new Error(error);
  });
  return handleResponse<T>(response);
}

function handleResponse<T>(response: Response) {
  if (!response.ok) throw new Error(response.statusText);
  return response.json().then(json => {
    return snakeCaseJsonToCamel(json) as T;
  });
}

//TODO: add a proper parser in the backend to allow the frontend to be used with any backend
const snakeCaseJsonToCamel = (json: Object): Object => {
  return Object.keys(json).map((key: string, value: any) => {
    return [key.replace(/([-_]\w)/g, g => g[1].toUpperCase()), value];
  });
};
