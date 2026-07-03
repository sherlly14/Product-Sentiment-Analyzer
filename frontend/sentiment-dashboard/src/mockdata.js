export const products = [
  {
    id: 1,
    name: "iPhone 15",
    rating: 4.5,
    sentimentData: [
      { name: "Positive", value: 60 },
      { name: "Neutral", value: 25 },
      { name: "Negative", value: 15 },
    ],
    ratingData: [
      { rating: "1★", count: 2 },
      { rating: "2★", count: 3 },
      { rating: "3★", count: 10 },
      { rating: "4★", count: 30 },
      { rating: "5★", count: 35 },
    ],
    reviews: [
      { id: 1, user: "Arun", text: "Great phone, battery super!", sentiment: "Positive" },
      { id: 2, user: "Divya", text: "Camera okay than", sentiment: "Neutral" },
    ],
  },
  {
    id: 2,
    name: "Samsung S24",
    rating: 4.2,
    sentimentData: [
      { name: "Positive", value: 40 },
      { name: "Neutral", value: 30 },
      { name: "Negative", value: 20 },
    ],
    ratingData: [
      { rating: "1★", count: 5 },
      { rating: "2★", count: 8 },
      { rating: "3★", count: 15 },
      { rating: "4★", count: 20 },
      { rating: "5★", count: 22 },
    ],
    reviews: [
      { id: 3, user: "Karthik", text: "Heating issue irukku", sentiment: "Negative" },
      { id: 4, user: "Meena", text: "Display semma nice", sentiment: "Positive" },
    ],
  },
  {
    id: 3,
    name: "OnePlus 13",
    rating: 4.3,
    sentimentData: [
      { name: "Positive", value: 50 },
      { name: "Neutral", value: 30 },
      { name: "Negative", value: 20 },
    ],
    ratingData: [
      { rating: "1★", count: 4 },
      { rating: "2★", count: 6 },
      { rating: "3★", count: 12 },
      { rating: "4★", count: 28 },
      { rating: "5★", count: 30 },
    ],
    reviews: [
      { id: 5, user: "Suresh", text: "Fast charging semma!", sentiment: "Positive" },
      { id: 6, user: "Priya", text: "Software updates konjam slow", sentiment: "Neutral" },
    ],
  },
  {
    id: 4,
    name: "Redmi Note 14",
    rating: 3.9,
    sentimentData: [
      { name: "Positive", value: 35 },
      { name: "Neutral", value: 35 },
      { name: "Negative", value: 30 },
    ],
    ratingData: [
      { rating: "1★", count: 8 },
      { rating: "2★", count: 10 },
      { rating: "3★", count: 18 },
      { rating: "4★", count: 15 },
      { rating: "5★", count: 14 },
    ],
    reviews: [
      { id: 7, user: "Vignesh", text: "Budget phone ku semma value", sentiment: "Positive" },
      { id: 8, user: "Lakshmi", text: "Heating problem konjam irukku", sentiment: "Negative" },
    ],
  },
];