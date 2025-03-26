import React, { useEffect, useState } from "react";
import { fetchProducts } from "../api/products";

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    const loadProducts = async () => {
      const data = await fetchProducts(page);
      if (data) {
        setProducts(data.products);
        setTotalPages(data.total_pages);
      }
    };
    loadProducts();
  }, [page]);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Product List</h1>
      <ul>
        {products.map((product) => (
          <li key={product.sku} className="border-b py-2">
            {product.product_name} - ${product.price}
          </li>
        ))}
      </ul>

      {/* Pagination Controls */}
      <div className="mt-4">
        <button
          onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
          disabled={page === 1}
          className="px-4 py-2 bg-gray-300 rounded mr-2"
        >
          Previous
        </button>

        <span>Page {page} of {totalPages}</span>

        <button
          onClick={() => setPage((prev) => Math.min(prev + 1, totalPages))}
          disabled={page === totalPages}
          className="px-4 py-2 bg-gray-300 rounded ml-2"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default ProductList;
