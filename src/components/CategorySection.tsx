export default function CategorySection() {
  return (
    <div className="bg-white p-6 rounded-2xl shadow-md">
      <h2 className="text-xl font-bold mb-4">
        Categories Overview
      </h2>

      <div className="flex flex-wrap gap-4">
        <span className="bg-red-100 text-red-600 px-4 py-2 rounded-full">
          🍕 Fast Food
        </span>

        <span className="bg-yellow-100 text-yellow-700 px-4 py-2 rounded-full">
          🍗 Chicken
        </span>

        <span className="bg-pink-100 text-pink-600 px-4 py-2 rounded-full">
          🍨 Desserts
        </span>
      </div>
    </div>
  );
}