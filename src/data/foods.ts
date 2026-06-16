import type { Food } from "../types/food";

import pizza from "../assets/pizza.jpg";
import burger from "../assets/burger.jpg";
import chicken from "../assets/chicken.jpg";
import icecream from "../assets/icecream.jpg";

export const foods: Food[] = [
  {
    id: 1,
    name: "Pizza",
    image: pizza,
    status: "🔥 Best Seller",
    category: "Fast Food",
  },
  {
    id: 2,
    name: "Burger",
    image: burger,
    status: "⭐ Popular",
    category: "Fast Food",
  },
  {
    id: 3,
    name: "Fried Chicken",
    image: chicken,
    status: "📈 Trending",
    category: "Chicken",
  },
  {
    id: 4,
    name: "Ice Cream",
    image: icecream,
    status: "🆕 New Favorite",
    category: "Dessert",
  },
];