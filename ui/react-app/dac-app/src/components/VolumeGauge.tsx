import {
    CircularProgressbar,
    buildStyles
} from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

export function VolumeGauge({ volume }: { volume: number }) {
    return (
        <div style={{ 'width': '70%', 'height': '70%' }}>
            <CircularProgressbar
                value={volume}
                text={`${volume}%`}
                styles={buildStyles({
                    pathColor: '#4ade80',
                    textColor: '#1f2937',
                })}
            />
        </div>
    );
}