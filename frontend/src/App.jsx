import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import ProductList from "./pages/ProductList";

function App() {
  return (
    <Router>
      <nav className="p-4 bg-gray-200">
        <Link to="/" className="mr-4">Home</Link>
        <Link to="/products">Products</Link>
      </nav>

      <Routes>
        <Route path="/" element={<h1 className="text-3xl">Welcome to ScrapeWithRian</h1>} />
        <Route path="/products" element={<ProductList />} />
      </Routes>
    </Router>
  );
}

export default App;
