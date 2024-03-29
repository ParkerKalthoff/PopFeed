import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function pop() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const { popid } = useParams();

  useEffect(() => {
    // Define a function to fetch data
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const jsonData = await response.json();
        setData(jsonData);
        setLoading(false);
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    // Call the function to fetch data when the component mounts
    fetchData();

    // Clean up function if needed (e.g., to cancel pending requests)
    return () => {
      // Cleanup logic here
    };
  }, []); // Empty dependency array ensures that the effect runs only once

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!data) return null;

  return (
    <div>
      <h2>Pop Component</h2>
      <p>popid: {popid}</p>
      {/* Render your data here */}
    </div>
  );
}

export default pop
