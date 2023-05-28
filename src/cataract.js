import React,{useState} from "react";

function Cataract(){
    const [selectedImage, setSelectedImage] = useState(null);

    const handleImageUpload = (event) => {
        setSelectedImage(event.target.files[0]);
    };

    const sendbackend=async(event)=>{
        if (selectedImage) {
            const formData = new FormData();
            formData.append('image', selectedImage);
      
            try {
              const response = await fetch('http://127.0.0.1:5000/eyedisease', {
                method: 'POST',
                body: formData,
              }).then(data=>{
                console.log(data);
              });
      
              if (response.ok) {
                console.log(response.body);
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

export default Cataract;