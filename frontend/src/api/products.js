import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; // Adjust this if deployed

export const fetchProducts = async (page = 1) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/products`, {
      params: { page },
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    return null; // Handle errors gracefully
  }
};
