export async function sendGet(endpoint: string) {
  return fetch(endpoint).then(response => response.json());
}
export async function sendPost(endpoint: string, data: string) {
  const response = await fetch(endpoint, {
    method: 'POST',
    body: data,
    headers: {
      "Content-type": "application/json"
    }
  });
  return response.json();

}
export async function sendPut(endpoint: string, data: string) {
  const response = await fetch(endpoint, {
    method: 'PUT',
    body: data,
    headers: {
      "Content-Type": "application/json"
    }
  });

  return response.json();

}

