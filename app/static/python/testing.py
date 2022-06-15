
"""

m = Marque(nom = "bmw")
db.session.add(m)
db.session.commit()

v = Voiture(
    modele = "Clio",
    annee = "2018",
    prix = "15000",
    kilometrage = "15000",
    nb_places = "5",
    nb_portes = "5",
    couleur = "rouge",
    carburant = "essence",
    puissance = "100",
    puissance_fiscale = "100",
    boite_vitesse = "manuelle",
    description = "description",
    marque_id = 1)
for i in range(5):
    v.images.append(Voiture_images(url = f"image {i}"))
db.session.add(v)
db.session.commit()

print(Voiture.query.all())
print(Marque.query.all())

marque_id = Voiture.query.all()[0].marque_id
print(f'marque " {Marque.query.get(marque_id).nom}')
"""



images = [
    [
    "https://upload.wikimedia.org/wikipedia/commons/3/32/2008_Volvo_C30_SE_Sport_D5_Automatic_2.0_Front.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f2/Volvo_c70_cabrio.jpg",
    "https://s3-eu-west-1.amazonaws.com/staticeu.izmocars.com/vehicleimages/640x480/dealers/planet_vo/337058253981_01_hd.jpg",
    "https://images.caradisiac.com/logos-ref/gamme/gamme--volvo-xc90/S7-gamme--volvo-xc90.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/3/32/2008_Volvo_C30_SE_Sport_D5_Automatic_2.0_Front.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f2/Volvo_c70_cabrio.jpg",
    "https://s3-eu-west-1.amazonaws.com/staticeu.izmocars.com/vehicleimages/640x480/dealers/planet_vo/337058253981_01_hd.jpg",
    "https://images.caradisiac.com/logos-ref/gamme/gamme--volvo-xc90/S7-gamme--volvo-xc90.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/3/32/2008_Volvo_C30_SE_Sport_D5_Automatic_2.0_Front.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f2/Volvo_c70_cabrio.jpg"
    ],
    [
    "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGNhcnN8ZW58MHx8MHx8&w=1000&q=80",
    "https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/chevrolet-camaro-red-track-1200x800-%281%29.jpg",
    "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDF8fHxlbnwwfHx8fA%3D%3D&w=1000&q=80",
    "https://cdn.pixabay.com/photo/2020/09/06/07/37/car-5548242__340.jpg",
    "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGNhcnN8ZW58MHx8MHx8&w=1000&q=80",
    "https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/chevrolet-camaro-red-track-1200x800-%281%29.jpg",
    "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDF8fHxlbnwwfHx8fA%3D%3D&w=1000&q=80",
    "https://cdn.pixabay.com/photo/2020/09/06/07/37/car-5548242__340.jpg",
    "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGNhcnN8ZW58MHx8MHx8&w=1000&q=80",
    "https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_cg_hero_large/v1/editorial/chevrolet-camaro-red-track-1200x800-%281%29.jpg"
    ],
    [
    "https://images.unsplash.com/photo-1606220838315-056192d5e927?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80",
    "https://apex4-production.s3.eu-west-1.amazonaws.com/tenant_efcfc251-f00b-487b-85fa-ca3aee1587ce/media/uploads/2016/photography-porsche-911-turbo.jpg",
    "https://www.adobe.com/content/dam/cc/us/en/creativecloud/photography/discover/car-photography/car-photography_fb-img_1200x800.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLd0OcIihNvnj8T3iYcQnAqnj5X0XpqcadvHAnv8EcfJC7JxGBzOvTpGRsf249p0dY4u8&usqp=CAU",
    "https://images.unsplash.com/photo-1606220838315-056192d5e927?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80",
    "https://apex4-production.s3.eu-west-1.amazonaws.com/tenant_efcfc251-f00b-487b-85fa-ca3aee1587ce/media/uploads/2016/photography-porsche-911-turbo.jpg",
    "https://www.adobe.com/content/dam/cc/us/en/creativecloud/photography/discover/car-photography/car-photography_fb-img_1200x800.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLd0OcIihNvnj8T3iYcQnAqnj5X0XpqcadvHAnv8EcfJC7JxGBzOvTpGRsf249p0dY4u8&usqp=CAU",
    "https://images.unsplash.com/photo-1606220838315-056192d5e927?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80",
    "https://apex4-production.s3.eu-west-1.amazonaws.com/tenant_efcfc251-f00b-487b-85fa-ca3aee1587ce/media/uploads/2016/photography-porsche-911-turbo.jpg"
    ],
    [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRoBc2w6SX7hgtq3g0Kd7Nlec9Exc6AZkjNNd23T7LdW4hLomiEgX6tSDM-YTDVASEy8E&usqp=CAU",
    "https://i.insider.com/533c883e6bb3f7e101b5b893?width=1000&format=jpeg&auto=webp",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnbDKGKDTbu43CarHsg62Voq7hvR1idJVsVQPHaF8_6OHLpQrmgW3AtBkK1uxCd2fmB0k&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsOkYzq8jzl7BlbZ2pk9KyxD9ctuwR52dcJZkFbGmfNDcB4_tRpy3tO8e8A6tW9qeslKY&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRoBc2w6SX7hgtq3g0Kd7Nlec9Exc6AZkjNNd23T7LdW4hLomiEgX6tSDM-YTDVASEy8E&usqp=CAU",
    "https://i.insider.com/533c883e6bb3f7e101b5b893?width=1000&format=jpeg&auto=webp",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnbDKGKDTbu43CarHsg62Voq7hvR1idJVsVQPHaF8_6OHLpQrmgW3AtBkK1uxCd2fmB0k&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsOkYzq8jzl7BlbZ2pk9KyxD9ctuwR52dcJZkFbGmfNDcB4_tRpy3tO8e8A6tW9qeslKY&usqp=CAU",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRoBc2w6SX7hgtq3g0Kd7Nlec9Exc6AZkjNNd23T7LdW4hLomiEgX6tSDM-YTDVASEy8E&usqp=CAU",
    "https://i.insider.com/533c883e6bb3f7e101b5b893?width=1000&format=jpeg&auto=webp"
    ]
]
