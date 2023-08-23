// Sample data for areas associated with different plants
const areasByPlant = {
    a: ['Area 1', 'Area 2', 'Area 3'],
    b: ['Area 4', 'Area 5', 'Area 6'],
  };
  
  function updateAreaOptions() {
    const plantSelect = document.getElementById('plant');
    const areaSelect = document.getElementById('area');
  
    // Clear previous options
    areaSelect.innerHTML = '<option value="">Select Area</option>';
  
    // Get the selected plant
    const selectedPlant = plantSelect.value;
  
    // If a plant is selected, populate the corresponding areas
    if (selectedPlant && areasByPlant[selectedPlant]) {
      areasByPlant[selectedPlant].forEach(area => {
        const option = document.createElement('option');
        option.value = area;
        option.text = area;
        areaSelect.appendChild(option);
      });
    }
  }