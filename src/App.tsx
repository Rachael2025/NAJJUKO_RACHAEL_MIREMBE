import DashboardHeader from "./components/DashboardHeader";
import FoodCard from "./components/FoodCard";
import CategorySection from "./components/CategorySection";
import { foods } from "./data/foods";

export default function App() {
  return (
    <div className="min-h-screen bg-amber-900 text-white p-8">
      <DashboardHeader />

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4 mb-10">
        {foods.map((food) => (
          <FoodCard key={food.id} food={food} />
        ))}
      </div>

      <CategorySection />
    </div>
  );
}

