import axios from 'axios';
export async function sendGet(endpoint) {
  const response = await axios.get(endpoint);
  return await response.data;
}
export async function sendPost(endpoint, data) {

  const response = await axios.post(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: data,
  });

  return await response.data;

}
