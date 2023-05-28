import React,{useState} from "react";

function Skin(){
    const [selectedImage, setSelectedImage] = useState(null);

    const handleImageUpload = (event) => {
        setSelectedImage(event.target.files[0]);
    };

    const sendbackend=async(event)=>{
        if (selectedImage) {
            const formData = new FormData();
            formData.append('image', selectedImage);
      
            try {
              const response = await fetch('http://127.0.0.1:5000/skindisease', {
                method: 'POST',
                body: formData,
              });
      
              if (response.ok) {
                console.log(response);
                console.log('Image uploaded successfully!');
              } else {
                console.error('Image upload failed.');
              }
            } catch (error) {
              console.error('Error occurred during image upload:', error);
            }
          } else {
            console.warn('No image selected.');
          }
    }

    return(
        <div>
            <input onChange={handleImageUpload} id="upload" type="file"/>
            <input onClick={sendbackend} id="submit" type="submit"/>
        </div>
    )
}

export default Skin;