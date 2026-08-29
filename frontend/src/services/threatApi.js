import axios from 'axios';

const API_BASE = 'http://127.0.0.1:8000';

export const fetchThreats = async () => {
  try {
    const res = await axios.get(`${API_BASE}/api/threats`);
    return res.data;
  } catch (err) {
    const res = await axios.get(`${API_BASE}/threats`);
    return res.data;
  }
};

export const postDetection = async (formData) => {
  try {
    const res = await axios.post(`${API_BASE}/api/detect`, formData);
    console.log("Backend Response:", res.data);
    return res.data;
  } catch (err) {
    console.error("API Post Error:", err.response ? err.response.data : err.message);
    throw err;
  }
};