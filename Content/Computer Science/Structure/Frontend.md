```
src/
├── main/
│   ├── main.jsx              # App entry point
│   ├── main.css              # Global styles, CSS resets
│   └── layout.jsx            # App shell (nav, footer, common layout)
│
├── home/
│   ├── home.jsx              # Home page component
│   ├── home.css              # Home-specific styles
│   └── api.ts                # Home-specific API calls
│
├── about/
│   ├── about.jsx
│   ├── about.css
│   └── api.ts
│
├── dashboard/
│   ├── dashboard.jsx         # Main dashboard component
│   ├── dashboard.css
│   ├── api.ts                # Dashboard API calls
│   └── components/           # Dashboard-specific components
│       ├── DashboardCard.jsx
│       ├── DashboardTable.jsx
│       └── StatsWidget.jsx
│
├── profile/
│   ├── profile.jsx
│   ├── profile.css
│   ├── api.ts
│   └── components/
│       ├── ProfileForm.jsx
│       └── AvatarUpload.jsx
│
├── shared/
│   ├── components/           # Reusable UI components
│   │   ├── Button/
│   │   │   ├── Button.jsx
│   │   │   └── Button.css
│   │   ├── Modal/
│   │   │   ├── Modal.jsx
│   │   │   └── Modal.css
│   │   ├── Input/
│   │   │   ├── Input.jsx
│   │   │   └── Input.css
│   │   └── index.js          # Barrel exports
│   │
│   ├── hooks/                # Custom React hooks
│   │   ├── useFetch.js
│   │   ├── useAuth.js
│   │   └── useLocalStorage.js
│   │
│   ├── utils/                # Helper functions
│   │   ├── formatters.js     # Date, currency, text formatters
│   │   ├── validators.js     # Form validation helpers
│   │   └── constants.js      # App-wide constants
│   │
│   ├── api.ts                # Shared API utilities (axios config, interceptors)
│   └── styles/               # Shared styles
│       ├── variables.css     # CSS custom properties
│       └── mixins.css        # Reusable CSS patterns
│
└── assets/
    ├── images/
    ├── icons/
    └── fonts/
```

## Key Benefits

- **Self-contained features**: Each page/feature has everything it needs in one place
- **Clear separation**: Page-specific code stays with the page, shared code is explicitly shared
- **Easy to scale**: New features just add a new folder
- **Easy to delete**: Remove a feature by deleting its folder
- **Intuitive navigation**: Developers know exactly where to look for code

## Conventions

- **Feature folders**: Named after the route/page (e.g., `/dashboard` → `dashboard/`)
- **Main component**: Always named after the folder (`dashboard.jsx` in `dashboard/`)
- **API files**: Keep API calls close to where they're used
- **Components subfolder**: Only when a feature needs multiple components
- **Shared components**: Follow folder-per-component pattern with co-located styles

## Example Usage

```jsx
// In dashboard/dashboard.jsx
import { fetchDashboardData } from './api'
import { Button } from '../shared/components'
import DashboardCard from './components/DashboardCard'
import './dashboard.css'

// In shared/components/index.js
export { Button } from './Button/Button'
export { Modal } from './Modal/Modal'
export { Input } from './Input/Input'
```