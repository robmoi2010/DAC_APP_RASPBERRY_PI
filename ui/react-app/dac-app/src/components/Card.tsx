export function Card({ children, className = '', ...props }) {
  return (
    <div
      className={`bg-white rounded-2xl shadow-md p-6 border border-gray-200 ${className}`}
      {...props}
    >
      {children}
    </div>
  );
}

export function CardHeader({ children }) {
  return <div className="mb-4 font-bold text-lg">{children}</div>;
}

export function CardContent({ children }) {
  return <div className="text-sm text-gray-700">{children}</div>;
}

export function CardFooter({ children }) {
  return <div className="mt-4 text-right">{children}</div>;
}