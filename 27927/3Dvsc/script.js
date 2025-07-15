import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

gsap.registerPlugin(ScrollTrigger);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5

const renderer = new THREE.WebGLRenderer(
    {
        alpha: true,
        antialias: true
    });

const start_place = document.getElementById('trigger1')
renderer.setSize(start_place.clientWidth, start_place.clientHeight);
start_place.appendChild(renderer.domElement);

// let controls = new OrbitControls(camera, renderer.domElement);

const loader = new GLTFLoader();

const pmremGenerator = new THREE.PMREMGenerator(renderer);
pmremGenerator.compileEquirectangularShader();

new RGBELoader()
    .setPath('') // путь к папке
    .load('buikslotermeerplein_4k.hdr', function (texture) {
        const envMap = pmremGenerator.fromEquirectangular(texture).texture;

        scene.environment = envMap;
        scene.background = null;   // если хочешь видеть фон HDRI (или убери эту строку)

        texture.dispose();
        pmremGenerator.dispose();
    });

let model

loader.load('Untitled.glb', function (gltf) {
    model = gltf.scene
    model.position.y = -1
    model.scale.set(0.5, 1, 0.5);
    scene.add(model);
}, undefined, function (error) {
    console.error(error);
});

function animate() {
    requestAnimationFrame(animate);
    // controls.update()
    renderer.render(scene, camera);
}
animate();


const triggers = ["trigger1", "trigger2", "trigger3", "trigger4"]

triggers.forEach((id, index) => {
    const el = document.getElementById(id)

    ScrollTrigger.create({
        trigger: el,
        start: "top center",
        end: "bottom center",
        scrub: true,
        onEnter: () => {

            const pos = get3DPositionFromDOM(el)

            gsap.to(model.position, {
                x: pos.x
            })

            if (index==0) {
                gsap.to(model.rotation, {
                    y: 0
                })
            }
            else if (index==1) {
                gsap.to(model.rotation, {
                    y: -1.5
                })
            }
            else if (index==2) {
                gsap.to(model.rotation, {
                    y: -3
                })
            }
            else if (index==3) {
                gsap.to(model.rotation, {
                    y: -4.5
                })
            }
        },
        onEnterBack: () => {

            const pos = get3DPositionFromDOM(el)

            gsap.to(model.position, {
                x: pos.x
            })

            if (index==0) {
                gsap.to(model.rotation, {
                    y: 0
                })
            }
            else if (index==1) {
                gsap.to(model.rotation, {
                    y: -1.5
                })
            }
            else if (index==2) {
                gsap.to(model.rotation, {
                    y: -3
                })
            }
            else if (index==3) {
                gsap.to(model.rotation, {
                    y: -4.5
                })
            }
        }
    })
})


// Convert DOM center to Three.js world coordinates
function get3DPositionFromDOM(domElement) {
  const rect = domElement.getBoundingClientRect();
  const x = rect.left + rect.width / 2;
  const y = rect.top + rect.height / 2;


  // normalized device coordinates (-1 to +1)
  const ndcX = (x / window.innerWidth) * 2 - 1;
  const ndcY = -(y / window.innerHeight) * 2 + 1;

  const ndcVector = new THREE.Vector3(ndcX, ndcY, 0.5).unproject(camera)
  const direction = ndcVector.sub(camera.position).normalize()
  const distance = -camera.position.z / direction.z
  const position = camera.position.clone().add(direction.multiplyScalar(distance))
  console.log(position)
  return position
}

window.addEventListener('resize', () => {
    renderer.setSize(start_place.clientWidth, start_place.clientHeight)
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
})