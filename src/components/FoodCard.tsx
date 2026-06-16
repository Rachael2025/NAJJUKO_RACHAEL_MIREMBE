import type{ Food } from "../types/food";

type Props = {
  food: Food;
};

export default function FoodCard({ food }: Props) {
  return (
    <div className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition">
      <img
        src={food.image}
        alt={food.name}
        className="w-full h-48 object-cover"
      />

      <div className="p-4">
        <h3 className="text-lg font-bold text-gray-800">
          {food.name}
        </h3>

        <p className="text-sm text-gray-500">
          {food.category}
        </p>

        <span className="inline-block mt-3 px-3 py-1 rounded-full bg-orange-100 text-orange-600 text-sm">
          {food.status}
        </span>
      </div>
    </div>
  );
}