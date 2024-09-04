# Error Management in Frontend

This document outlines the current approach to error management in the frontend of our application.

## Overview

We use a combination of React Query (Tanstack Query) for API calls and a custom hook for displaying error toasts. This separation of concerns allows for centralized error handling and consistent error display across the application.

## Key Components

### 1. useErrorToast Hook

Location: `frontend/src/hooks/useErrorToast.ts`

This custom hook provides a reusable way to display error toasts using Chakra UI's toast system.