import React,{useState} from "react";

function Reportannotation(){
    const [selectedImage, setSelectedImage] = useState(null);

    const handleImageUpload = (event) => {
        setSelectedImage(event.target.files[0]);
    };

    const sendbackend=async(event)=>{
        if (selectedImage) {
            const formData = new FormData();
            formData.append('image', selectedImage);
      
            try {
              const response = await fetch('/api/upload', {
                method: 'POST',
                body: formData,
              });
      
              if (response.ok) {
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

export default Reportannotation;