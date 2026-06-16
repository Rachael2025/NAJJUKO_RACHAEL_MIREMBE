
export type FoodStatus =
  | "🔥 Best Seller"
  | "⭐ Popular"
  | "📈 Trending"
  | "🆕 New Favorite";

export interface Food {
  id: number;
  name: string;
  image: string;
  status: FoodStatus;
  category: string;
}