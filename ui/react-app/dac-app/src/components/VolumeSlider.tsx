import * as Slider from '@radix-ui/react-slider';
const VolumeSlider = () => {
    return (
        <Slider.Root
            value={[10]}
            onValueChange={() => { }} // note this expects array
            max={100}
            step={1}
            aria-label="Volume"
            className="relative flex items-center select-none touch-none w-64 h-5"
        >
            <Slider.Track className="bg-gray-300 relative grow rounded-full h-1">
                <Slider.Range className="absolute bg-blue-500 rounded-full h-full"/>
            </Slider.Track>
            <Slider.Thumb className="block w-4 h-4 bg-white border border-gray-400 rounded-full shadow hover:bg-gray-100"/>
        </Slider.Root>
    );
}
export default VolumeSlider;